const adminDb = db.getSiblingDB('admin');

adminDb.createUser({
  user: process.env.MONGO_USER,
  pwd: process.env.MONGO_PASSWORD,
  roles: [
    { role: 'dbOwner', db: process.env.MONGO_DB }
  ]
});

const userDb = db.getSiblingDB(process.env.MONGO_DB);

print('MongoDB initialized');
