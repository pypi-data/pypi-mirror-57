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

module.exports = ReactopyaModel;