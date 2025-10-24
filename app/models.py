from sqlmodel import SQLModel, Field, Relationship

# 学校情報テーブル
class School(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    img: str
    name: str
    description: str

    # リレーションシップ: 1対多（学校は複数のブースとイベントを持つ）
    booths: list["Booth"] = Relationship(back_populates="school")
    events: list["Event"] = Relationship(back_populates="school")

# ブース情報テーブル
class Booth(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    schoolid: int = Field(foreign_key="school.id")
    major: str
    img: str
    name: str
    description: str

    # リレーションシップ: 多対1（ブースは1つの学校に属する）
    school: School = Relationship(back_populates="booths")

# イベント情報テーブル
class Event(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    schoolid: int = Field(foreign_key="school.id")
    major: str
    location: str
    time_start: str
    time_end: str
    img: str
    name: str
    description: str

    # リレーションシップ: 多対1（イベントは1つの学校に属する）
    school: School = Relationship(back_populates="events")
