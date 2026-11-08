"""会飞、会倒豆奶的豆奶包。运行：python3 dounaibao.py。"""
from dataclasses import dataclass

VERSION = "1.0.0"
FLIGHT_HEIGHT_CM = 30
POUR_SPEED_ML_PER_SECOND = 40
CUP_GRIP_HANDS = 2
CUP_TILT_DEGREES = 10


@dataclass(frozen=True)
class PourResult:
    requested_ml: int
    served_ml: int
    spilled_ml: int


def fly(height_cm=FLIGHT_HEIGHT_CM):
    if height_cm <= 0:
        raise ValueError("飞行高度必须大于零")
    return f"豆奶包飞到了 {height_cm} 厘米高"


def pour_soymilk(amount_ml=200):
    if amount_ml <= 0:
        raise ValueError("豆奶量必须大于零")
    stable = CUP_GRIP_HANDS >= 2 and CUP_TILT_DEGREES <= 15
    spilled_ml = 0 if stable else round(amount_ml * 0.25)
    return PourResult(amount_ml, amount_ml - spilled_ml, spilled_ml)


if __name__ == "__main__":
    print(f"会飞的豆奶包 v{VERSION}")
    print(fly())
    result = pour_soymilk()
    print(f"倒出 {result.requested_ml} ml，接住 {result.served_ml} ml，洒出 {result.spilled_ml} ml")
