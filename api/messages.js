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
    const db = getDb();
    const today = new Date().toISOString().slice(0, 10);

    const selectByDate = db.prepare(
      `SELECT author, text, created_at AS timestamp
       FROM messages
       WHERE board = ? AND substr(created_at, 1, 10) = ?
       ORDER BY datetime(created_at) DESC
       LIMIT 3`
    );

    let rows = selectByDate.all('central', today);

    // If there are no messages for today, fall back to the most recent date available.
    if (rows.length === 0) {
      const latestDateRow = db
        .prepare(
          `SELECT substr(created_at, 1, 10) AS date_only
           FROM messages
           WHERE board = ?
           ORDER BY datetime(created_at) DESC
           LIMIT 1`
        )
        .get('central');
      if (latestDateRow && latestDateRow.date_only) {
        rows = selectByDate.all('central', latestDateRow.date_only);
      }
    }

    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    return res.status(200).json({ messages: rows });
  } catch (err) {
    console.error('Failed to read messages from sqlite database', err);
    return res.status(500).json({ error: 'Failed to read messages' });
  }
};
