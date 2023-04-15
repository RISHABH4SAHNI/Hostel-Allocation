var mysql = require("mysql");
const util = require("util");
const fs = require("fs");

var con = {
  host: "localhost", //host edit here
  user: "root", //user edit here
  password: "Admin@123", //password edit here
  database: "BITS",
};

const dataSql = fs.readFileSync("./sqlFile.sql").toString();

function makeDb(config) {
  const connection = mysql.createConnection(config);
  return {
    query(sql, args) {
      return util.promisify(connection.query).call(connection, sql, args);
    },
    close() {
      return util.promisify(connection.end).call(connection);
    },
  };
}

async function initialise(con) {
  let db = makeDb(con);
  const dataArr = dataSql.toString().split(";");

  try {
    dataArr.forEach((query) => {
      if (query) {
        // Add the delimiter back to each query before you run them
        // In my case the it was `);`
        query += ";";
        db.query(query);
      }
    });
  } catch (err) {
    console.log(err);
  } finally {
    await db.close();
  }
}

initialise(con);
