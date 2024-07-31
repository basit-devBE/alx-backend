import { createClient } from 'redis';

const client = createClient();

client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.connect().catch(console.error);

const setNewSchool = async (schoolName, value) => {
    try {
        await client.set(schoolName, value);
        console.log(`Set ${schoolName} to ${value}`);
    } catch (err) {
        console.log(err);
    }
}

const displaySchoolValue = async (schoolName) => {
    try {
        const value = await client.get(schoolName);
        console.log(`${schoolName}: ${value}`);
    } catch (err) {
        console.log(err);
    }
}

// Call the functions in proper order
(async () => {
    await displaySchoolValue('Holberton');  // This will likely be null or undefined if not set before
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
