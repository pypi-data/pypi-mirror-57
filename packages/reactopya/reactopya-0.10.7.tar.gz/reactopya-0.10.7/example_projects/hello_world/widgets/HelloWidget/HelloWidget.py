class HelloWidget:
    def __init__(self):
        super().__init__()

    def javascript_state_changed(self, prev_state, state):
        self._set_status('running', 'Running HelloWidget')

        # Processing code goes here
        # The state argument contains the state set from the javacript code
        # In .js file, use this.pythonInterface.setState({...})

        x = state.get('x', None)
        self._set_state(
            output='The value of x is {}'.format(x)
        )

        self._set_status('finished', 'Finished HelloWidget')

    def on_message(self, msg):
        # process custom messages from JavaScript here
        # In .js file, use this.pythonInterface.sendMessage({...})
        self._send_message(dict(
            name='message_received',
            msg=msg
        ))
    
    # Send a custom message to JavaScript side
    # In .js file, use this.pythonInterface.onMessage((msg) => {...})
    def _send_message(self, msg):
        self.send_message(msg)

    # Set the python state
    def _set_state(self, **kwargs):
        self.set_state(kwargs)
    
    # Set error status with a message
    def _set_error(self, error_message):
        self._set_status('error', error_message)
    
    # Set status and a status message. Use running', 'finished', 'error'
    def _set_status(self, status, status_message=''):
        self._set_state(status=status, status_message=status_message)