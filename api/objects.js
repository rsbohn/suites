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
    const rows = getDb()
      .prepare(
        `SELECT name, description, location
         FROM objects
         ORDER BY name ASC`
      )
      .all();

    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    return res.status(200).json({ objects: rows });
  } catch (err) {
    console.error('Failed to read objects from sqlite database', err);
    return res.status(500).json({ error: 'Failed to read objects' });
  }
};
