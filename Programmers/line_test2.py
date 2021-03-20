# 2021. 03.20 라인 코테 2교시 단계적 구현
def check_arg(flag):
    global com_split
    args = []

    if not com_split:  # 인자가 없는데, 명령어가 -e이 아니라면 False
        if rule_arr[flag] != "NULL":
            return False
    else:
        # arg를 명령어를 만나기 전까지 집어넣어
        while com_split:
            now_str = com_split.pop(0)
            if now_str in rule_arr:
                com_split.insert(0, now_str)
                break
            else:
                args.append(now_str)

        if len(args) == 1:
            if args[0].isdigit():  # 인자가 정수인데, 명령어 규칙이 NUMBERS가 아니라면 False
                if rule_arr[flag] not in ["NUMBERS", "NUMBER"]:
                    return False
            elif args[0].isalpha():  # 인자가 알파벳인데, 명령어 규칙이 STRINGS가 아니라면 False
                if rule_arr[flag] not in ["STRINGS", "STRING"]:
                    return False

        elif len(args) > 1:
            for arg in args:
                if arg.isdigit():  # 인자가 정수인데, 명령어 규칙이 NUMBERS가 아니라면 False
                    if rule_arr[flag] != "NUMBERS":
                        return False
                elif arg.isalpha():  # 인자가 알파벳인데, 명령어 규칙이 STRINGS가 아니라면 False
                    if rule_arr[flag] != "STRINGS":
                        return False

    return True


def check(command, program):
    global com_split

    com_split = command.split()  # 공백을 기준으로 잘라서 저장
    if com_split.pop(0) != program:  # 프로그램 이름과 다르면 False 리턴
        return False

    while com_split:  # com_split이 비어있지 않은동안 반복
        flag = com_split.pop(0)
        if flag not in rule_arr:  # 없는 명령어라면, False
            return False
        else:  # 존재하는 명령어라면, 인자를 체크
            if not check_arg(flag):  # 인자가 적절하지 않으면 False
                return False
    return True


def solution(program, flag_rules, commands):
    result = []
    for flag_rule in flag_rules:  # flag 규칙들을 딕셔너리형태로 저장
        arr = flag_rule.split()
        rule_arr[arr[0]] = arr[1]

    for command in commands:  # 커멘트를 하나씩 확인
        result.append(check(command, program))

    return result


program = "trip"
flag_rules = ["-days NUMBERS", "-dest STRING"]
commands = ["trip -days 15 10 -dest Seoul Paris", "trip -days 10 -dest Seoul"]

# program = "line"
# flag_rules = ["-s STRINGS", "-n NUMBERS", "-e NULL"]
# commands = ["line -n 100 102 -s hi -e", "line -n id pwd -n 100"]


rule_arr = {}
com_split = []

print(solution(program, flag_rules, commands))

