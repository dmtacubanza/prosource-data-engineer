class inMemDB:
    def __init__(self):
        self.data = {}
        self.transactions = []
        self.transaction_pointer = -1

    def set(self, key, val):
        self.data[key] = val
        print(f"SET {key} => {val}")

    def get(self, key):
        value = self.data.get(key, "NULL")
        print(f"GET {key} => {value}")

    def delete(self, key):
        if key in self.data:
            del self.data[key]
            print(f"DELETE {key}")
        else:
            print(f"Cannot find the key: {key}")

    def count(self, val):
        count = list(self.data.values()).count(val)
        print(f"COUNT {val} => {count}")

    def begin(self):
        self.transaction_pointer += 1
        self.transactions.append(dict(self.data))
        print("BEGIN")

    def rollback(self):
        if self.transaction_pointer >= 0:
            self.data = dict(self.transactions[self.transaction_pointer])
            self.transactions.pop()
            self.transaction_pointer -= 1
            print("ROLLBACK")
        else:
            print("This transaction cannot be found.")

    def commit(self):
        self.transactions = []
        self.transaction_pointer = -1
        print("COMMIT")

    def end_database(self):
        print("END")
        exit()

def main():
    db = inMemDB()

    while True:
        try:
            user_input = input().split()
            command = user_input[0]

            if command == "SET":
                db.set(user_input[1], user_input[2])
            elif command == "GET":
                db.get(user_input[1])
            elif command == "DELETE":
                db.delete(user_input[1])
            elif command == "COUNT":
                db.count(user_input[1])
            elif command == "BEGIN":
                db.begin()
            elif command == "ROLLBACK":
                db.rollback()
            elif command == "COMMIT":
                db.commit()
            elif command == "END":
                db.end_database()
                break
            else:
                print("NOT a valid command. Here are the valid commands: SET, GET, DELETE, COUNT, BEGIN, ROLLBACK, COMMIT, and END.")

        except IndexError:
            print("Sorry but the input is invalid.")
        except KeyboardInterrupt:
            print("\nDatabase exit.")
            break

if __name__ == "__main__":
    main()
