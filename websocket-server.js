function sleep(d){
  for(var t = Date.now();Date.now() - t <= d;);
}

var amqp = require('amqp');  
var WebSocketServer = require('ws').Server,
wss = new WebSocketServer({ port: 8181 });
wss.on('connection', function (ws) {
    console.log('client connected');
    ws.on('message', function (message) {
        console.log('fffff');
        console.log(message);
    });
    for(var t = Date.now();Date.now() - t <= 1000;);
    console.log('kkkkkkk')
    //ws.send('ffffff')
});

sleep(5000); //当前方法暂停5秒
//wss.send('pop')
console.log('0000000')
console.log(wss.clients.length)
wss.clients.forEach(function each(client) {
      console.log('1111111')
      if (client !== ws && client.readyState === WebSocket.OPEN) {
        console.log('222222')
        client.send('fffffkkkkkk');
      }
});

var connection = amqp.createConnection({url: "amqp://hardchain:pswHd@localhost:5672/%2F"});
// Wait for connection to become established.
connection.on('ready', function () {
    var callbackCalled = false;
    exchange = connection.exchange('xxx', {type: 'direct',autoDelete:false});
    connection.queue("electron3",{autoDelete:false}, function(queue){
        queue.bind('xxx','electron3', function() {
            //exchange.publish('electron3', 'this is message is testing ......');
             callbackCalled = true;
        });

        queue.subscribe(function (message) {
          console.log('At 5 second recieved message is:'+ message.data);
          wss.clients.forEach(function each(client){
              console.log('11111')
              client.send('fffffak')
          });
        });

    });
});
