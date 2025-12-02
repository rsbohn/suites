const path = require('path');
const Database = require('better-sqlite3');

const board = process.argv[2] || 'central';
const limitArg = process.argv[3];
const limit = Number.isInteger(Number(limitArg)) ? Number(limitArg) : 20;

const dbPath = path.join(__dirname, '..', 'data', 'field.db');
const db = new Database(dbPath, { readonly: true });

const rows = db
  .prepare(
    `SELECT board, author, text, created_at
     FROM messages
     WHERE board = ?
     ORDER BY datetime(created_at) DESC
     LIMIT ?`
  )
  .all(board, limit);

if (rows.length === 0) {
  console.log(`No messages found for board "${board}".`);
  process.exit(0);
}

rows.forEach((row, idx) => {
  const header = `${idx + 1}. [${row.board}] ${row.author} @ ${row.created_at}`;
  console.log(header);
  console.log(row.text);
  console.log(''); // blank line between entries
});
