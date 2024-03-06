import client from './0-redis_client.js';
import redis from 'redis';

function createHash() {
    client.hset('HolbertonSchools', 'Portland', 50, redis.print);
    client.hset('HolbertonSchools', 'Seattle', 80, redis.print);
    client.hset('HolbertonSchools', 'New York', 20, redis.print);
    client.hset('HolbertonSchools', 'Bogota', 20, redis.print);
    client.hset('HolbertonSchools', 'Cali', 40, redis.print);
    client.hset('HolbertonSchools', 'Paris', 2, redis.print);
}

function displayHash(key) {
    client.hgetall(key, (_err, reply) => {
        console.log(reply);
    });
}

createHash();
displayHash('HolbertonSchools');
