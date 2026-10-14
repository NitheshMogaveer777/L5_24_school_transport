"""School bus transport register."""
import sqlite3


def create_connection():
    """Create the riders database."""
    connection = sqlite3.connect(":memory:")
    connection.execute(
        """
        CREATE TABLE riders (
            id INTEGER PRIMARY KEY,
            student TEXT,
            route TEXT,
            stop TEXT,
            fee INTEGER
        )
        """
    )
    return connection


conn = create_connection()


def enroll_rider(student, route, stop, fee):
    """Enroll a student on a bus route."""
    conn.execute(
        """
        INSERT INTO riders (student, route, stop, fee)
        VALUES (?, ?, ?, ?)
        """,
        (student, route, stop, fee),
    )
    conn.commit()


def route_roster(route):
    """Return the names of students on a route."""
    result = conn.execute(
        "SELECT student FROM riders WHERE route = ?",
        (route,),
    )
    return [row[0] for row in result]


def export_roster(path, route):
    """Export a route roster to a text file."""
    with open(path, "w", encoding="utf-8") as output_file:
        for name in route_roster(route):
            output_file.write(name + "\n")


def dispatch_alert(route):
    """Print a bus dispatch alert."""
    print(f"dispatching bus {route}")


def fee_collected(route):
    """Calculate the total fees for a route."""
    result = conn.execute(
        "SELECT SUM(fee) FROM riders WHERE route = ?",
        (route,),
    ).fetchone()
    return result[0] or 0


def main():
    """Run the transport register demonstration."""
    enroll_rider("Tara", "R1", "Lake Road", 1800)
    enroll_rider("Kabir", "R1", "Mill Street", 1800)
    enroll_rider("Zoya", "R2", "Fort Gate", 2100)

    assert fee_collected("R1") == 3600

    export_roster("route_r1.txt", "R1")
    dispatch_alert("R1")
    print(route_roster("R2"))


if __name__ == "__main__":
    main()
