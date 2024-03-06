import { expect } from 'chai';
import kue from 'kue';
import createPushNotificationsJobs from './8-job';

describe('createPushNotificationsJobs', () => {
    let queue;

    beforeEach(() => {
        queue = kue.createQueue();
        queue.testMode.enter();
    });

    afterEach(() => {
        queue.testMode.clear();
        queue.testMode.exit();
    });

    it('display a error message if jobs is not an array', () => {
        expect(() => createPushNotificationsJobs(null, queue)).to.throw('Jobs is not an array');
    });

    it('create two new jobs to the queue', () => {
        const jobs = [
            {
                phoneNumber: '4153518780',
                message: 'This is the code 1234 to verify your account'
            },
            {
                phoneNumber: '4153518781',
                message: 'This is the code 4562 to verify your account'
            }
        ];

        createPushNotificationsJobs(jobs, queue);

        expect(queue.testMode.jobs.length).to.equal(2);

        const job1 = queue.testMode.jobs[0];
        expect(job1.type).to.equal('push_notification_code_3');
        expect(job1.data.phoneNumber).to.equal('4153518780');
        expect(job1.data.message).to.equal('This is the code 1234 to verify your account');

        const job2 = queue.testMode.jobs[1];
        expect(job2.type).to.equal('push_notification_code_3');
        expect(job2.data.phoneNumber).to.equal('4153518781');
        expect(job2.data.message).to.equal('This is the code 4562 to verify your account');
    });
});

