const express = require('express');
const app = express();
const http = require('http');
const server = http.createServer(app);
const io = require('socket.io')(server)

app.set('port', process.env.PORT || 3000)

app.get('/', (req, res) => {
    res.send('home');
});

io.on('connection', socket => {
  console.log('se ha conectao')

  socket.on('message', info => {
    console.log(info)
    io.sockets.emit('new_message', JSON.stringify(info))
  })

  socket.on('disconnect', () => {
    console.log('user disconnected')
  })
})

server.listen(app.get('port'), () => {
    console.log(`server on port ${app.get('port')}`);
});
