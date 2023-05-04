
package main

import (
    "fmt"
    "database/sql"
    _ "go-sql-driver/mysql"
)

func main() {
    fmt.Println("Go MySQL Tutorial")

    // Open up our database connection.
    // The database is called testDb
    db, err := sql.Open("mysql", "allan2:allan2@tcp(1192.168.122.206:3306)/newDB")

    // if there is an error opening the connection, handle it
    if err != nil {
        panic(err.Error())
    }
}
