let soc = null
const commands = {}

window.onload = () => {
    soc = new WebSocket("ws://{{ mindspace.hostname }}:{{ mindspace.websocket_port }}")
    soc.onmessage = e => {
        let data = JSON.parse(e.data)
        let command = commands[data.command]
        command(...data.args)
    }
    soc.command = (name, args, kwargs) => {
        if (args === undefined) {
            args = []
        }
        if (kwargs === undefined) {
            kwargs = {}
        }
        let data = [name, args, kwargs]
        let s = JSON.stringify(data)
        soc.send(s)
    }
}
