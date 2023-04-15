var mysql = require("mysql");
const util = require("util");

var con = {
  host: "localhost", //host edit here
  user: "root", //user edit here
  password: "Admin@123", // password edit here
  database: "BITS",
};
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

async function getSID(con) {
  let SID;
  let db = makeDb(con);
  try {
    let S_ID = await db.query("SELECT S_ID FROM Wing");
    SID = S_ID.map((S_ID) => S_ID.S_ID);
  } catch (err) {
    console.log(err);
  } finally {
    await db.close();
    return SID;
  }
}

async function getSIDRow(con, sID) {
  let row;
  let db = makeDb(con);
  try {
    row = await db.query("SELECT * FROM Wing WHERE S_ID = " + sID);
  } catch (err) {
    // handle the error
  } finally {
    await db.close();
    return row[0];
  }
}

async function getRoomOccupancy(con, hostelName) {
  let status;
  let db = makeDb(con);
  try {
    let STATUS_OF_OCCUPANCY = await db.query(
      'SELECT STATUS_OF_OCCUPANCY FROM Rooms WHERE H_NAME = "' +
        hostelName +
        '"' /*AND ROOM_NUMBER = ' +
        roomNo*/
    );
    status = STATUS_OF_OCCUPANCY.map(
      (STATUS_OF_OCCUPANCY) => STATUS_OF_OCCUPANCY.STATUS_OF_OCCUPANCY
    );
  } catch (err) {
    console.log(err);
    // handle the error
  } finally {
    await db.close();
    return status;
  }
  // con.end();
}

async function insertInAllotment(con, sid, hname, rnum) {
  let x;
  let y;
  let db = makeDb(con);
  try {
    x = await db.query(
      "INSERT INTO Allotment VALUES (" +
        sid[0] +
        ', "' +
        hname +
        '",' +
        rnum +
        "),(" +
        sid[1] +
        ', "' +
        hname +
        '",' +
        rnum +
        "),(" +
        sid[2] +
        ', "' +
        hname +
        '",' +
        (rnum + 1) +
        "),(" +
        sid[3] +
        ', "' +
        hname +
        '",' +
        (rnum + 1) +
        "),(" +
        sid[4] +
        ', "' +
        hname +
        '",' +
        (rnum + 2) +
        "),(" +
        sid[5] +
        ', "' +
        hname +
        '",' +
        (rnum + 2) +
        ")"
    );
    y = await db.query(
      "UPDATE Rooms SET STATUS_OF_OCCUPANCY = " +
        1 +
        " WHERE ROOM_NUMBER = " +
        rnum +
        " AND H_NAME = " +
        '"' +
        hname +
        '" OR ROOM_NUMBER = ' +
        (rnum + 1) +
        " AND H_NAME = " +
        '"' +
        hname +
        '" OR ROOM_NUMBER = ' +
        (rnum + 2) +
        " AND H_NAME = " +
        '"' +
        hname +
        '"'
    );
    // console.log(await getRoomOccupancy(con, hname));
    // console.log(x);
  } catch (err) {
    // handle the error
    console.log(err);
  } finally {
    await db.close();
    // return status;
  }
  // con.end();
}

async function resetAllotmentTable(con) {
  let x;
  let y;
  let z;
  let db = makeDb(con);
  try {
    x = await db.query("DROP TABLE Allotment");
    y = await db.query(
      "CREATE TABLE Allotment(S_ID int not null, H_NAME CHAR(20) not null, ROOM_NUMBER int not null,primary key(S_ID))"
    );
    z = await db.query("UPDATE Rooms SET STATUS_OF_OCCUPANCY = " + 0);
  } catch (err) {
    // handle the error
  } finally {
    await db.close();
    // return status;
  }
}

async function allotment(con) {
  const sid = await getSID(con); // gets all the S_ID in Wing table to iterate through

  await resetAllotmentTable(con);
  var status_V = await getRoomOccupancy(con, "Vyas");
  var status_R = await getRoomOccupancy(con, "Ram");
  var status_B = await getRoomOccupancy(con, "Budh");
  var status_K = await getRoomOccupancy(con, "Krishna");
  var status_G = await getRoomOccupancy(con, "Gandhi");
  sid.forEach(async (sids) => {
    let row = await getSIDRow(con, sids); // gets a row of the Wing table with S_ID
    let studentIds = [
      row.S_ID,
      row.S_ID1,
      row.S_ID2,
      row.S_ID3,
      row.S_ID4,
      row.S_ID5,
    ];
    let hostelPref = row.Preference;
    var status;
    if (hostelPref == "Vyas") status = status_V;
    if (hostelPref == "Ram") status = status_R;
    if (hostelPref == "Budh") status = status_B;
    if (hostelPref == "Krishna") status = status_K;
    if (hostelPref == "Gandhi") status = status_G;

    let rnum = 1;
    while (status[rnum - 1]) {
      rnum += 3;
    }
    if (rnum <= 60) {
      // 60 is MAX CAPACITY
      status[rnum - 1] = 1;
      status[rnum] = 1;
      status[rnum + 1] = 1;
      await insertInAllotment(con, studentIds, hostelPref, rnum); //inserts in the allotment table and sets room occupancy to true
    }

    if (hostelPref == "Vyas") status_V = status;
    if (hostelPref == "Ram") status_R = status;
    if (hostelPref == "Budh") status_B = status;
    if (hostelPref == "Krishna") status_K = status;
    if (hostelPref == "Gandhi") status_G = status;
  });
}

allotment(con);
