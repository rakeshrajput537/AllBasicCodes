const app = require("express")();
const server = require("http").Server(app);
const io = require('socket.io')(server);
const users = {};
const connections = {};
io.on('connection', (socket) => {
	const ip = handleIP(socket.handshake.address);
	connections[ip] = socket;
	socket.emit('selfIP',ip);
	if(users[ip] === undefined) {
		users[ip] = [];
	}
		io.emit('connectedIPs',Object.keys(users));
	socket.on('messageSend', (req) => {
		const receiver = connections[req.to];
		if(receiver !== undefined)
		receiver.emit('messageRecieve', {
			'from': ip,
			'message': req.message
		});
	});
	socket.on('openChat', (connectIP, response) => {
		if(users[ip].findIndex(connectIP) == -1)
		users[ip].push(ip);
	connections[connectIP].emit('okok');
		respone('ok');
	});
	socket.on('disconnect', () => {
	});

});
server.listen(3001, () => {
	console.log('listening on 3000');
});
function handleIP(ip) {
    if(ip === '::1') {
        return '127.0.0.1';
    } else if(ip.substr(0,7) === '::ffff:') {
        return ip.slice(7);
    }
    return ip;

}