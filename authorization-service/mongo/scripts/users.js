//
// Users
//

db = db.getSiblingDB('users');

// Test purpose, of course it shouldn't be here
db.users.insertMany([
    {name: 'random', password: 'random'},
    {name: 'blabla', password: 'blabla'},
    {name: 'tati', password: 'tata'},
    {name: 'gandalf', password: 'thegrey'},
    {name: 'gandalf2', password: 'thewhite'},
]);

// unique index on the name
db.users.createIndex(
    {name: 1},
    {unique: true}
);