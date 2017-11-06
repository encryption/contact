import Contact from '../src/contact';

test('Contact calls send email', async () => {
  console.log(jest);
  let fakeSend = jest.fn();
  let req = {
    body: { test: true },
    get: () => false,
  };
  let res = {
    redirect: () => true,
    status: () => this,
    send: () => true,
  };
  await Contact(fakeSend)({ req, res });

  expect(fakeSend.mock.calls).toEqual(1);
});
