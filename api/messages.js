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
        `SELECT author, text, created_at AS timestamp
         FROM messages
         WHERE board = ?
         ORDER BY id DESC
         LIMIT 3`
      )
      .all('central');

    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    return res.status(200).json({ messages: rows });
  } catch (err) {
    console.error('Failed to read messages from sqlite database', err);
    return res.status(500).json({ error: 'Failed to read messages' });
  }
};
