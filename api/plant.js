const path = require('path');
const Database = require('better-sqlite3');

let db;

function getDb() {
  if (!db) {
    const dbPath = path.join(__dirname, '..', 'data', 'field.db');
    db = new Database(dbPath, { readonly: true });
  }
  return db;
}

module.exports = (req, res) => {
  try {
    const row = getDb()
      .prepare('SELECT name, description FROM plants LIMIT 1')
      .get();

    if (!row) {
      return res.status(404).json({ error: 'No plant found' });
    }

    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    return res.status(200).json({ name: row.name, description: row.description });
  } catch (err) {
    console.error('Failed to read sqlite database', err);
    return res.status(500).json({ error: 'Failed to read sqlite database' });
  }
};
