import base64
import os
import importlib
import time
import logging
import uuid
import numpy as np
from .reactopyacolabwidget import ReactopyaColabWidget
from .reactopyaelectronwidget import ReactopyaElectronWidget
from .reactopyahostedwidget import ReactopyaHostedWidget
from .init import _get_init_info
from .host_widget import host_widget
from .reactopyacomponent import ReactopyaComponent
from .reactopya_serialize import reactopya_serialize, reactopya_deserialize

logger = logging.getLogger('reactopya')


class _BaseWidget:
    def __init__(self, WidgetOrig, widget_type, project_name, *args, **kwargs):
        self._project_name = project_name
        self._widget_type = widget_type
        self._props = dict(**kwargs)
        self._children = {}
        self._child_ids = []
        for i, ch in enumerate(list(args)):
            self._children[str(i)] = ch
            self._child_ids.append(str(i))
        self._connect_children(self._children)
        self._component = ReactopyaComponent(WidgetOrig)
        self._component.on_python_state_changed(
            lambda state: self._handle_python_state_changed(state))
        self._component.on_send_custom_message(
            lambda message: self._handle_send_custom_message(message))
        self._reactopya_widget = None
        self._javascript_state = dict()  # for snapshot
        self._python_state = dict()  # for snapshot
        self._running_process = False  # for run_process_mode
        self._python_state_changed_handlers = []
        self._send_custom_message_handlers = []
        self._is_dynamic_child=False
        # self._component._initial_update()
    
    def _set_dynamic_child(self, val):
        self._is_dynamic_child = val

    def _connect_children(self, children):
        for child_id, ch in children.items():
            self._connect_child(str(child_id), ch)

    def _connect_child(self, child_id, child):
        logger.info('WIDGET:%s:_connect_child %s', self._widget_type, child_id)
        child_id = str(child_id)
        child.on_python_state_changed(
            lambda state: self._handle_python_state_changed(dict(_childId=child_id, state=state)))
        child.on_send_custom_message(
            lambda message: self._handle_send_custom_message(dict(_childId=child_id, message=message)))

    def _handle_python_state_changed(self, state):
        logger.info('WIDGET:%s:_handle_python_state_changed', self._widget_type)
        if '_childId' not in state:
            for key, val in state.items():
                self._python_state[key] = val  # for snapshot
        if self._reactopya_widget:
            self._reactopya_widget.set_python_state(state)
        if self._running_process:
            msg = {"name": "setPythonState", "state": state}
            self._send_message_to_parent_process(msg)
        for handler in self._python_state_changed_handlers:
            handler(state)
    
    def _handle_send_custom_message(self, message):
        logger.info('WIDGET:%s:_handle_send_custom_message', self._widget_type)
        if self._reactopya_widget:
            self._reactopya_widget.send_custom_message(message)
        if self._running_process:
            msg = {"name": "customMessage", "message": message}
            self._send_message_to_parent_process(msg)
        for handler in self._send_custom_message_handlers:
            # i don't think this is used
            handler(message)
    
    def on_python_state_changed(self, handler):
        self._python_state_changed_handlers.append(handler)
    
    def on_send_custom_message(self, handler):
        # I don't think this is used
        self._send_custom_message_handlers.append(handler)

    
    # internal function to send message to javascript component
    def _send_message_to_parent_process(self, msg):
        msg = reactopya_serialize(msg)
        import simplejson
        txt = simplejson.dumps(msg, ignore_nan=True)
        msg_path = os.path.join(self._run_process_mode_dirpath, '{}.msg-from-python'.format(self._run_process_mode_message_index))
        self._run_process_mode_message_index = self._run_process_mode_message_index + 1
        try:
            write_text_file(msg_path + '.tmp', txt)
            os.rename(msg_path + '.tmp', msg_path)
        except:
            print('WARNING: unable to write file: {}'.format(msg_path))

    def _handle_javascript_state_changed(self, state):
        logger.info('WIDGET:%s:_handle_javascript_state_changed: %s %s', self._widget_type, state, self._children.keys())
        if '_childId' in state:
            child_id = str(state['_childId'])
            if child_id in self._children:
                self._children[str(child_id)]._handle_javascript_state_changed(state['state'])
            else:
                logger.error('WIDGET:%s:_handle_javascript_state_changed:Child %s not found', self._widget_type, child_id)
            return
        for key, val in state.items():
            self._javascript_state[key] = val  # for snapshot
        self._component._handle_javascript_state_changed(state)
    
    def _handle_custom_message(self, message):
        if '_childId' in message:
            child_id = str(message['_childId'])
            if child_id in self._children:
                self._children[str(child_id)]._handle_custom_message(message['message'])
            else:
                logger.error('WIDGET:%s:_handle_custom_message:Child %s not found', self._widget_type, child_id)
            return
        self._component._handle_custom_message(message)
    
    def _handle_add_child(self, child_id, project_name, type, is_dynamic_child):
        logger.info('WIDGET:%s:_handle_add_child: child_id=%s project_name=%s type=%s', self._widget_type, child_id, project_name, type)
        child_id = str(child_id)
        WIDGET = _get_widget_class_from_type(project_name, type)
        W = WIDGET()
        if is_dynamic_child:
            W._set_dynamic_child(True)
        self._connect_child(child_id, W)
        self._children[str(child_id)] = W
        self._child_ids.append(str(child_id))
        logger.info('WIDGET:%s:_handle_add_child finished: child_id=%s project_name=%s type=%s', self._widget_type, child_id, project_name, type)
        return W

    def _serialize(self, include_javascript_state=False, include_python_state=False, include_bundle_fname=False, child_id=''):
        children_serialized = []
        for child_id in self._child_ids:
            children_serialized.append(
                self._children[str(child_id)]._serialize(
                    include_javascript_state=include_javascript_state,
                    include_python_state=include_python_state,
                    include_bundle_fname=include_bundle_fname,
                    child_id=child_id
                )
            )
        obj = dict(
            project_name=self._project_name,
            type=self._widget_type,
            children=children_serialized,
            props=reactopya_serialize(self._props),
            is_dynamic_child=self._is_dynamic_child,
            child_id=child_id
        )
        if include_javascript_state:
            obj['javascript_state'] = reactopya_serialize(self._javascript_state)
        if include_python_state:
            obj['python_state'] = reactopya_serialize(self._python_state)
        if include_bundle_fname:
            dirname = os.path.dirname(os.path.realpath(__file__))
            obj['bundle_fname'] = os.path.join(dirname, 'dist', 'bundle.js')

        return obj

    def show(self, **kwargs):
        init_info = _get_init_info()
        if os.getenv('REACTOPYA_SERVER_SESSION_DIR', None):
            RW = ReactopyaHostedWidget
            init_info['mode'] = 'hosted'
        else:
            if init_info['mode'] == 'jupyter':
                from reactopya_jup import ReactopyaJupyterWidget
                RW = ReactopyaJupyterWidget
            elif init_info['mode'] == 'colab':
                RW = ReactopyaColabWidget
            elif init_info['mode'] == 'electron':
                RW = ReactopyaElectronWidget
            else:
                raise Exception('You need to initialize spikeforest_widgets via one of the following: init_jupyter() or init_electron()')
        self._reactopya_widget = RW(
            project_name=self._project_name,
            type=self._widget_type,
            initial_children=[
                self._children[str(child_id)]._serialize(child_id=child_id)
                for child_id in self._child_ids
            ],
            props=self._props
        )
        if init_info['mode'] == 'colab':
            self._reactopya_widget._set_bundle_js(
                init_info['bundle_js'], store_bundle_in_notebook=init_info['store_bundle_in_notebook'])
        elif init_info['mode'] == 'electron':
            self._reactopya_widget._set_bundle_fname(init_info['bundle_fname'])
            self._reactopya_widget._set_electron_src(init_info['electron_src'])
        elif init_info['mode'] == 'hosted':
            session_id = os.getenv('REACTOPYA_SERVER_SESSION_ID')
            session_dir = os.getenv('REACTOPYA_SERVER_SESSION_DIR')
            html = self.export_snapshot(
                output_fname=None,
                format='html',
                use_python_backend_websocket=True,
                session_id=session_id
            )
            self._reactopya_widget._set_snapshot_html(html)
            self._reactopya_widget._set_session_dir(session_dir)
            self._reactopya_widget._set_session_id(session_id)
        self._reactopya_widget.on_javascript_state_changed(
            self._handle_javascript_state_changed)
        self._reactopya_widget.on_custom_message(
            self._handle_custom_message)
        self._reactopya_widget.on_add_child(
            self._handle_add_child_data
        )

        return self._reactopya_widget.show(**kwargs)
    
    def host(self, *, port):
        raise Exception('Method host() no longer supported. Use reactopya_server instead.')
        # host_widget(self._serialize(), port=port)

    def run_process_mode(self, dirpath):
        self._start_process_mode(dirpath)
        while self._iterate_process_mode():
            time.sleep(0.01)
    
    def _iterate_process_mode(self):
        try:
            messages = self._read_messages(self._run_process_mode_dirpath)
        except:
            if not os.path.exists(self._run_process_mode_dirpath):
                # Stopping process because directory no longer exists
                return False
            messages = []
        if len(messages) > 0:
            for msg in messages:
                self._handle_message_process_mode(msg)
        else:
            self._component.iterate()
        if self._quit:
            return False
        return True
            
    def _start_process_mode(self, dirpath):
        self._run_process_mode_dirpath = dirpath
        self._run_process_mode_message_index = 100000
        self._running_process = True
        self._quit = False

    
    def _read_messages(self, dirname):
        import simplejson
        messages = []
        files = os.listdir(dirname)
        files = sorted(files)
        for file in files:
            if file.endswith('.msg-from-js'):
                fname = os.path.join(dirname, file)
                with open(fname, 'r') as f:
                    msg = simplejson.load(f)
                msg = reactopya_deserialize(msg)
                messages.append(msg)
                os.remove(fname)
                break  # only one at a time for now
        return messages

    
    def _initial_update(self):
        self._component._initial_update()
        for ch in self._children.values():
            ch._initial_update()
    
    def add_serialized_children(self, children):
        for i, child in enumerate(children):
            child_id = child.get('child_id', str(i))
            W = self._handle_add_child(
                child_id,
                child.get('project_name', self._project_name),
                child['type'],
                child.get('is_dynamic', False)
            )
            child_children = child.get('children', [])
            if len(child_children) > 0:
                W.add_serialized_children(child_children)
    
    def _handle_add_child_data(self, data):
        logger.info('WIDGET:%s:_handle_add_child_data: %s', self._widget_type, data)
        if '_childId' in data:
            child_id = str(data['_childId'])
            self._children[str(child_id)]._handle_add_child_data(data['data'])
            return
        self._handle_add_child(data['childId'], data['projectName'], data['type'], data.get('isDynamic', False))
    
    # internal function to handle incoming message (coming from javascript component)
    def _handle_message_process_mode(self, msg):
        if msg['name'] == 'setJavaScriptState':
            self._handle_javascript_state_changed(msg['state'])
        elif msg['name'] == 'customMessage':
            self._handle_custom_message(msg['message'])
        elif msg['name'] == 'addChild':
            self._handle_add_child_data(msg['data'])
        elif msg['name'] == 'quit':
            self._quit = True
        else:
            print(msg)
            raise Exception('Unexpected message in _handle_message_process_mode: {}'.format(msg['name']))

    def export_snapshot(self, output_fname, *, format, use_python_backend_websocket=False, session_id=''):
        import simplejson
        if format is not 'html':
            raise Exception('Unsupported format: {}'.format(format))
        serialized_widget = self._serialize(
            include_javascript_state=True, include_python_state=True, include_bundle_fname=True)
        project_names = _get_all_project_names(serialized_widget)
        project_bundle_fnames = _get_project_bundle_fnames(serialized_widget)
        snapshot = dict(
            serialized_widget=serialized_widget,
            project_names=project_names,
            project_bundles=[_read_text_file(
                project_bundle_fnames[project_name]) for project_name in project_names]
        )

        html = '''
<!DOCTYPE html>
<html>

<head>
    <meta charset="utf-8" />

    <!-- Disable caching by browser -->
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="Expires" content="0">

    <title></title>

    <style>
        body {
            font-family: sans-serif;
            margin: 0;
            padding: 0;
        }

        #root {
            height: 100vh;
            width: 100vw;

            display: flex;
            flex-direction: column;
            overflow: hidden;

            margin: 0px;
            padding: 0px;

            /* background: #b8c1c3; */
        }
    </style>
</head>

<body>
    <span>Loading html file...</span>
    <script type="text/javascript">

/*
This file is duplicated between
* reactopya_jup/lib/ReactopyaModel.js and
* reactopya/templates/__project_name___dev/src/components/ReactopyaModel.js
* reactopya/templates/__project_name__/__project_name__/electron/src/ReactopyaModel.js
* reactopya/templates/__project_name___bundle/ReactopyaModel.js
Only edit the one in
reactopya/templates/__project_name___dev/src/components/ReactopyaModel.js
Other edits will get overwritten when you run

> reactopya/devel/sync_code.py

*/

class ReactopyaModel {
    constructor(projectName, type) {
        this._projectName = projectName;
        this._type = type;

        this._pythonStateStringified = {};
        this._javaScriptStateStringified = {};
        this._childModels = {};

        this._pythonStateChangedHandlers = [];
        this._javaScriptStateChangedHandlers = [];
        this._sendCustomMessageHandlers = [];
        this._customMessageHandlers = [];
        this._childModelAddedHandlers = [];
        this._startHandlers = [];
        this._stopHandlers = [];
        this._running = false;
    }
    projectName() {
        return this._projectName;
    }
    type() {
        return this._type;
    }

    setPythonState(state) {
        if (state._childId) {
            this._childModels[state._childId + ''].setPythonState(state.state);
            return;
        }
        state = _reactopya_deserialize(state);
        this._setStateHelper(state, this._pythonStateStringified, this._pythonStateChangedHandlers);
    }
    setJavaScriptState(state) {
        this._setStateHelper(state, this._javaScriptStateStringified, this._javaScriptStateChangedHandlers);
    }
    getPythonState() {
        let ret = {};
        for (let key in this._pythonStateStringified) {
            ret[key] = _reactopya_deserialize(JSON.parse(this._pythonStateStringified[key]));
        }
        return ret;
    }
    getJavaScriptState() {
        let ret = {};
        for (let key in this._javaScriptStateStringified) {
            ret[key] = JSON.parse(this._javaScriptStateStringified[key]);
        }
        return ret;
    }
    addChildModelsFromSerializedChildren(children) {
        for (let i in children) {
            let child = children[i];
            let chmodel = this.addChild(i, child.project_name || this._projectName, child.type, false);
            chmodel.addChildModelsFromSerializedChildren(child.children || []);
        }
    }
    addChild(childId, projectName, type, isDynamic) {
        // if ((childId + '') in this._childModels) {
        //     return this._childModels[childId + ''];
        // }
        let model = new ReactopyaModel(projectName, type);
        model.onJavaScriptStateChanged((state) => {
            for (let handler of this._javaScriptStateChangedHandlers) {
                handler({
                    _childId: childId,
                    state: state
                });
            }
        });
        model.onSendCustomMessage((msg) => {
            for (let handler of this._sendCustomMessageHandlers) {
                handler({
                    _childId: childId,
                    message: msg
                });
            }
        });
        model.onChildModelAdded((data) => {
            for (let handler of this._childModelAddedHandlers) {
                handler({
                    _childId: childId,
                    data: data
                });
            }
        });
        model.onStart(() => {
            this.start();
        });
        model.onStop(() => {
            // actually we don't stop just because a child stopped!
            // this.stop();
        });
        this._childModels[childId + ''] = model;
        for (let handler of this._childModelAddedHandlers) {
            handler({
                childId: childId,
                projectName: projectName,
                type: type,
                isDynamic: isDynamic
            });
        }
        return model;
    }
    sendCustomMessage(message) {
        if (message._childId) {
            this._childModels[state._childId + ''].sendCustomMessage(message.message);
            return;
        }
        for (let handler of this._sendCustomMessageHandlers) {
            handler(message);
        }
    }
    childModel(childId) {
        return this._childModels[childId + ''];
    }
    start() {
        // the following two lines would mess up html snapshots
        // this._pythonStateStringified = {};
        // this._javaScriptStateStringified = {};
        for (let handler of this._startHandlers)
            handler();
    }
    stop() {
        this._running = false;
        for (let handler of this._stopHandlers)
            handler();

        // is this going to cause a problem?
        this._pythonStateStringified = {};
        this._javaScriptStateStringified = {};
        this._childModels = {};
    }
    onPythonStateChanged(handler) {
        this._pythonStateChangedHandlers.push(handler);
    }
    onJavaScriptStateChanged(handler) {
        this._javaScriptStateChangedHandlers.push(handler);
    }
    onSendCustomMessage(handler) {
        this._sendCustomMessageHandlers.push(handler);
    }
    onCustomMessage(handler) {
        this._customMessageHandlers.push(handler);
    }
    onChildModelAdded(handler) {
        this._childModelAddedHandlers.push(handler);
    }
    onStart(handler) {
        this._startHandlers.push(handler);
    }
    onStop(handler) {
        this._stopHandlers.push(handler);
    }
    handleCustomMessage(message) {
        if (message._childId) {
            this._childModels[message._childId + ''].handleCustomMessage(message.message);
            return;
        }
        message = _reactopya_deserialize(message);
        for (let handler of this._customMessageHandlers) {
            handler(message);
        }
    }
    _setStateHelper(state, existingStateStringified, handlers) {
        let changedState = {};
        let somethingChanged = false;
        for (let key in state) {
            let val = state[key];
            let valstr = JSON.stringify(val);
            if (valstr !== existingStateStringified[key]) {
                existingStateStringified[key] = valstr;
                changedState[key] = JSON.parse(valstr);
                somethingChanged = true;
            }
        }
        if (somethingChanged) {
            for (let handler of handlers) {
                handler(changedState);
            }
        }
    }
}

function _reactopya_deserialize(x) {
    if (!x) return x;
    if (Array.isArray(x)) {
        let ret = [];
        for (let i in x) {
            ret.push(_reactopya_deserialize(x[i]));
        }
        return ret;
    }
    else if (typeof(x) == 'object') {
        if ((x._reactopya_type) && (x._reactopya_type === '@reactopya-ndarray@')) {
            let ret = _reactopya_deserialize_ndarray(x);
            return ret;
        }
        else {
            let ret = {};
            for (let k in x) {
                ret[k] = _reactopya_deserialize(x[k]);
            }
            return ret;
        }
    }
    else {
        return x;
    }
}

function _reactopya_deserialize_ndarray(x) {
    window.debug_x = x;
    let TA
    if (x.dtype == 'float64') {
        TA = Float64Array;
    }
    else if (x.dtype == 'float32') {
        TA = Float32Array;
    }
    else if (x.dtype == 'int64') {
        // the problem is that BigInt cannot be JSON-serialized.
        // TA = BigInt64Array;
        throw new Error('Cannot handle int64. This should have been converted to float64 on the python side.');
    }
    else if (x.dtype == 'int32') {
        TA = Int32Array;
    }
    else if (x.dtype == 'int16') {
        TA = Int16Array;
    }
    else if (x.dtype == 'int8') {
        TA = Int8Array;
    }
    else if (x.dtype == 'uint64') {
        // the problem is that BigInt cannot be JSON-serialized.
        // TA = BigUint64Array;
        throw new Error('Cannot handle uint64. This should have been converted to float64 on the python side.');
    }
    else if (x.dtype == 'uint32') {
        TA = Uint32Array;
    }
    else if (x.dtype == 'uint16') {
        TA = Uint32Array;
    }
    else if (x.dtype == 'uint8') {
        TA = Uint8Array;
    }
    else {
        throw new Error(`Datatype not yet supported in _reactopya_deserialize_ndarray: ${x.dtype}`);
    }
    let data_1d = new TA(Uint8Array.from(atob(x.data_b64), c => c.charCodeAt(0)).buffer);
    // important to convert to regular array so it can be JSON-serialized properly later on
    data_1d = Array.from(data_1d);
    return _make_ndarray(x.shape, data_1d);
}

function _make_ndarray(shape, data_1d) {
    let prod_shape = 1;
    for (let i in shape) prod_shape *= shape[i];
    if (prod_shape != data_1d.length) {
        console.warn('shape = ', shape);
        throw new Error(`Unexpected size of data ${prod_shape} != ${data_1d.length}`);
    }
    if (shape.length === 1) {
        return data_1d;
    }
    else {
        let ret = [];
        let stride = 1;
        for (let i = 1; i < shape.length; i++) stride *= shape[i];
        for (let i = 0; i < prod_shape; i += stride) {
            ret.push(_make_ndarray(shape.slice(1), data_1d.slice(i, i + stride)));
        }
        return ret;
    }
}

ReactopyaModel.reactopya_deserialize = _reactopya_deserialize;



var snapshot = get_snapshot_json_b64();
snapshot = JSON.parse(atob(snapshot));
for (let js of snapshot.project_bundles) {
    eval(js);
}
window.snapshot=snapshot;

var sw = snapshot.serialized_widget;
let model = create_reactopya_model(sw);
attach_reactopya_model(sw, model);
// set_init_state_on_props(sw);

const verbose = false;

if (([use_python_backend_websocket]) && (window.location.host)) {
    class WebsocketClient {
        constructor() {
            if (verbose) console.info('WebsocketClient constructor');
            this._validationConfirmed = false;
            this._connected = false;
            this._pendingMessages = [];
            this._messageHandlers = [];
        }
        connect(url) {
            if (verbose) console.info('WebsocketClient connect', url);
            if ((typeof(window) !== 'undefined') && (window.WebSocket)) {
                this._ws = new window.WebSocket(url);
                this._ws.addEventListener('open', () => {
                    this._connected = true;
                    // this._sendMessage({message_type: 'validation', validation_string: 'reactopya-1'});
                    this._sendMessage({message_type: 'validation', validation_string: 'reactopya-2', session_id: '[session_id]'});
                });
                this._ws.addEventListener('message', (evt) => {this._handleMessage(evt.data);});
            }
            else {
                console.error('Cannot connect to websocket -- window.WebSocket is not defined');
            }
        }
        close() {
            if (this._ws) {
                this._ws.close();
            }
        }
        send(msg) {
            if (verbose) console.info('WebsocketClient send', msg);
            let message = {
                message_type: 'to_python_process',
                message: msg
            }
            if (this._validationConfirmed) {
                this._sendMessage(message);
            }
            else {
                this._pendingMessages.push(message);
            }
        }
        onMessage(handler) {
            this._messageHandlers.push(handler);
        }
        _handleMessage(message) {
            let msg;
            try {
                msg = JSON.parse(message);
            }
            catch(err) {
                console.error('Error parsing JSON message.');
                this._ws.terminate();
                return;
            }
            if (verbose) console.info('WebsocketClient _handleMessage', msg);
            if (msg.message_type == 'validation_confirmed') {
                this._validationConfirmed = true;
                for (let message of this._pendingMessages) {
                    this._sendMessage(message);
                }
                this._pendingMessages = [];
            }
            else if (msg.message_type == 'from_python_process') {
                for (let handler of this._messageHandlers) {
                    handler(msg.message);
                }
            }
            else {
                console.error('Unexpected message type in _handleMessage of WebsocketClient: ' + msg.message_type);
            }
        }
        
        _sendMessage(message) {
            this._ws.send(JSON.stringify(message));
        }
    }

    let client = new WebsocketClient();
    client.connect('ws://' + window.location.host);
    keepAlive();
    function keepAlive() {
        setTimeout(function() {
            client.send({
                name: 'keepAlive'
            });
            keepAlive();
        }, 15000);
    }

    model.onJavaScriptStateChanged(function(state) {
        if (verbose) console.info('model.onJavaScriptStateChanged', state);
        client.send({
            name: 'setJavaScriptState',
            state: state
        });
    });

    model.onSendCustomMessage(function(msg) {
        if (verbose) console.info('model.onSendCustomMessage', msg);
        client.send({
            name: 'customMessage',
            message: msg
        });
    });

    // important that this comes after we have added the initial children to the model
    model.onChildModelAdded(function(data) {
        if (verbose) console.info('model.onChildModelAdded', data);
        client.send({
            name: 'addChild',
            data: data
        });
    });

    client.onMessage(function(msg) {
        const name = msg.name;
        if (name == 'initialize') {
            //
        }
        else if (name == 'setPythonState') {
            let state = msg.state;
            if (verbose) console.info('setPythonState', state);
            model.setPythonState(state);
        }
        else if (name == 'customMessage') {
            let message = msg.message;
            if (verbose) console.info('customMessage', message);
            model.handleCustomMessage(message);
        }
        else {
            console.error(`Unrecognized message from from websocket client: ${name}`, msg);
        }
    });
}
else {
    window.reactopya.python_backend_disabled = true;
}

document.body.innerHTML=''; // remove the loading message
var div = document.createElement('div');
div.id = 'root';
document.body.appendChild(div);
window.reactopya.widgets[sw.project_name][sw.type].render(
    div,
    sw.children,
    sw.props,
    sw.key || '',
    sw.reactopyaModel || null,
    {
        fullBrowser: true
    }
);

function create_reactopya_model(serialized_widget) {
    let ret = new ReactopyaModel(serialized_widget.project_name, serialized_widget.type);
    create_reactopya_model_2(serialized_widget, ret);
    return ret;

    function create_reactopya_model_2(serialized_widget, model) {
        model.setJavaScriptState(serialized_widget.javascript_state || {});
        model.setPythonState(serialized_widget.python_state || {});
        for (let child of serialized_widget.children) {
            let child_id = child.child_id;
            let child_model = model.addChild(child_id, child.project_name, child.type, child.is_dynamic);
            create_reactopya_model_2(child, child_model);
        }
        return model;
    }
}

function attach_reactopya_model(serialized_widget, model) {
    serialized_widget.reactopyaModel = model;
    for (let child of serialized_widget.children) {
        let child_id = child.child_id;
        if (!child.is_dynamic) {
            let child_model = model.childModel(child_id);
            attach_reactopya_model(child, child_model);
        }
    }
}

function get_snapshot_json_b64() {
    return "[snapshot_json_b64]";
}

    </script>
</body>

</html>
        '''
        html = html.replace('[snapshot_json_b64]', base64.b64encode(simplejson.dumps(snapshot, ignore_nan=True).encode('utf-8')).decode())
        html = html.replace('[session_id]', session_id)
        html = html.replace('[use_python_backend_websocket]', 'true' if use_python_backend_websocket else 'false')
        if output_fname is not None:
            with open(output_fname, 'w') as f:
                f.write(html)
        else:
            return html

def _get_all_project_names(serialized_widget):
    ret = []
    ret.append(serialized_widget['project_name'])
    for ch in serialized_widget.get('children', []):
        ret = ret + _get_all_project_names(ch)
    return list(set(ret))  # unique elements of array


def _get_project_bundle_fnames(serialized_widget):
    ret = dict()
    ret[serialized_widget['project_name']] = serialized_widget['bundle_fname']
    for ch in serialized_widget.get('children', []):
        a = _get_project_bundle_fnames(ch)
        for key, val in a.items():
            ret[key] = val
    return ret


def _read_text_file(fname):
    with open(fname, 'r') as f:
        return f.read()

def write_text_file(fname, txt):
    with open(fname, 'w') as f:
        f.write(txt)

def _get_widget_class_from_type(project_name, type):
    mod = importlib.import_module(project_name)
    WIDGET = getattr(mod, type)
    return WIDGET