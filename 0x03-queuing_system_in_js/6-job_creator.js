import kue from 'kue';

const queue = kue.createQueue();

const jobData = {
    phoneNumber: 'A phone number',
    message: 'A notification'
};

const job = queue.create('push_notification_code', jobData);

job.on('enqueue', () => {
    console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => {
    console.log('Notification job completed');
});

job.on('failed', () => {
    console.log('Notification job failed');
});

job.save();