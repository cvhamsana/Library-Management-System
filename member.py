class Member:
    def __init__(self, member_id, name, email, phone):
        self.member_id = member_id
        self.name = name
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "member_id": self.member_id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @staticmethod
    def from_dict(data):
        return Member(
            data["member_id"],
            data["name"],
            data["email"],
            data["phone"]
        )