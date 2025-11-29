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
    const { date } = req.query || {};

    const stmt = date
      ? getDb().prepare(
          `SELECT date, condition, temperature_c, precipitation_chance, note
           FROM weather
           WHERE date = ?
           ORDER BY id DESC
           LIMIT 1`
        )
      : getDb().prepare(
          `SELECT date, condition, temperature_c, precipitation_chance, note
           FROM weather
           ORDER BY date DESC, id DESC
           LIMIT 1`
        );

    const row = date ? stmt.get(date) : stmt.get();

    if (!row) {
      return res.status(404).json({ error: 'No weather found' });
    }

    res.setHeader('Cache-Control', 's-maxage=60, stale-while-revalidate=120');
    return res.status(200).json({ weather: row });
  } catch (err) {
    console.error('Failed to read weather from sqlite database', err);
    return res.status(500).json({ error: 'Failed to read weather' });
  }
};
