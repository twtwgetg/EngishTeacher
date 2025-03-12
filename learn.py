import random

# 初始化生词列表和每个单词的记忆得分
vocabulary = {}

def add_word():
    """
    此函数用于添加新的生词到词汇表中
    """
    word = input("请输入要添加的生词: ")
    if word not in vocabulary:
        vocabulary[word] = 0  # 初始记忆得分设为0
        print(f"{word} 已成功添加到词汇表中。")
    else:
        print(f"{word} 已经在词汇表中。")

def practice():
    """
    此函数用于进行词组句练习
    """
    if not vocabulary:
        print("词汇表为空，请先添加一些生词。")
        return
    # 根据记忆得分生成权重，得分越低，权重越高
    weights = [1 / (score + 1) for score in vocabulary.values()]
    word = random.choices(list(vocabulary.keys()), weights=weights)[0]
    sentence = input(f"请用 {word} 组一个句子: ")
    if sentence:
        print(f"你组的句子是: {sentence}")
        # 询问用户是否记住了这个单词
        remember = input("你是否记住了这个单词？(y/n): ").lower()
        if remember == 'y':
            vocabulary[word] += 1  # 增加记忆得分
            print(f"好的， {word} 的记忆得分已增加。")
        else:
            print(f"没关系，继续努力学习 {word}。")

def main():
    """
    主函数，提供用户交互界面
    """
    while True:
        print("\n请选择操作:")
        print("1. 添加生词")
        print("2. 进行词组句练习")
        print("3. 退出")
        choice = input("请输入选项编号: ")
        if choice == '1':
            add_word()
        elif choice == '2':
            practice()
        elif choice == '3':
            print("感谢使用，再见！")
            break
        else:
            print("无效的选项，请重新输入。")

if __name__ == "__main__":
    main()