var xmlrpc = require('xmlrpc')
var elevator = xmlrpc.createClient({ host: 'localhost', port: 8000 })

const call = (method, ...args) => (
  new Promise((resolve, reject) => {
    elevator.methodCall(method, args, (error, value) => {
      if (error) return reject(error);
      return resolve(value);
    });
  })
);
module.exports = {
    call,
};
