
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
    db, err := sql.Open("mysql", "root:password1@tcp(127.0.0.1:3306)/test")

    // if there is an error opening the connection, handle it
    if err != nil {
        panic(err.Error())
    }
}
