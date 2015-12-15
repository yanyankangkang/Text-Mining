from stemming.porter2 import stem

vocabulary = {}
vocabularyStem = {}
vocabularyPrev = {}
vocabularySuff = {}
n = 1
k = 2

def removePunctuation(fileContent):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in fileContent:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

# def getVocabularyAll(content,k):
#     vocabulary = {}
#     index = 0
#     for i in range(len(content)):
#         if content[i] not in vocabulary:
#             vocabulary[content[i]] = index
#             index = index + 1
#         if stem(content[i]) not in vocabulary:
#             vocabulary[stem(content[i])] = index
#             index = index + 1
#         if k > len(content[i]):
#             s = content[i]
#         else:
#             s = content[i][:k]
#         if s not in vocabulary:
#             vocabulary[s] = index
#             index = index + 1
#         if k > len(content[i]):
#             s = content[i]
#         else:
#             s = content[i][-k:]
#         if s not in vocabulary:
#             vocabulary[s] = index
#             index = index + 1
#     print len(vocabulary)
#     return vocabulary


def getVocabulary(content):
    vocabulary = {}
    index = 0
    for i in range(len(content)):
        if content[i] not in vocabulary:
            vocabulary[content[i]] = index
            index = index + 1
    return vocabulary

def getVocabularyStem(content):
    vocabulary = {}
    index = 0
    for i in range(len(content)):
        if stem(content[i]) not in vocabulary:
            vocabulary[stem(content[i])] = index
            index = index + 1
    return vocabulary

def getVocabularyPrev(content,k):
    vocabulary = {}
    index = 0
    for i in range(len(content)):
        if k > len(content[i]):
            s = content[i]
        else:
            s = content[i][:k]
        if s not in vocabulary:
            vocabulary[s] = index
            index = index + 1
    return vocabulary

def getVocabularySuff(content,k):
    vocabulary = {}
    index = 0
    for i in range(len(content)):
        if k > len(content[i]):
            s = content[i]
        else:
            s = content[i][-k:]
        if s not in vocabulary:
            vocabulary[s] = index
            index = index + 1
    return vocabulary


def writeFeatureVector(content,label, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, k, output):
    f_output = open(output, 'w+')
    # size = len(vocabulary)
    # print size
    for i in range(len(content)):
        fVec_token = writeFVHelper(content, i, vocabulary, n, k, 0)
        fVec_stem = writeFVHelper(content, i, vocabularyStem, n, k, 1)
        fVec_prev = writeFVHelper(content, i, vocabularyPrev, n, k, 2)
        fVec_suff = writeFVHelper(content, i, vocabularySuff, n, k, 3)
        offset = 0
        for j in range(len(fVec_token)):
            fVec_token[j] = fVec_token[j] + offset
            offset = offset + len(vocabulary)
        for j in range(len(fVec_stem)):
            fVec_stem[j] = fVec_stem[j] + offset
            offset = offset + len(vocabularyStem)
        for j in range(len(fVec_prev)):
            fVec_prev[j] = fVec_prev[j] + offset
            offset = offset + len(vocabularyPrev)
        for j in range(len(fVec_suff)):
            fVec_suff[j] = fVec_suff[j] + offset
            offset = offset + len(vocabularySuff)
        fVec = fVec_token+fVec_stem+fVec_prev+fVec_suff
        if len(label) > 0:
            f_output.write((label[i]) + ',')
        for j in range(len(fVec) - 1):
            f_output.write(str(fVec[j]) + ',')
        f_output.write(str(fVec[len(fVec)-1]) + '\n')
    f_output.close()

def getFeatureVector(content, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, k):
    fVecs = []
    # size = len(vocabulary)
    # print size
    for i in range(len(content)):
        fVec_token = writeFVHelper(content, i, vocabulary, n, k, 0)
        fVec_stem = writeFVHelper(content, i, vocabularyStem, n, k, 1)
        fVec_prev = writeFVHelper(content, i, vocabularyPrev, n, k, 2)
        fVec_suff = writeFVHelper(content, i, vocabularySuff, n, k, 3)
        offset = 0
        for j in range(len(fVec_token)):
            fVec_token[j] = fVec_token[j] + offset
            offset = offset + len(vocabulary)
        for j in range(len(fVec_stem)):
            fVec_stem[j] = fVec_stem[j] + offset
            offset = offset + len(vocabularyStem)
        for j in range(len(fVec_prev)):
            fVec_prev[j] = fVec_prev[j] + offset
            offset = offset + len(vocabularyPrev)
        for j in range(len(fVec_suff)):
            fVec_suff[j] = fVec_suff[j] + offset
            offset = offset + len(vocabularySuff)
        fVec = fVec_token+fVec_stem+fVec_prev+fVec_suff
        fVecs.append(fVec)
    return fVecs

# def writeFeatureVector(content,label, vocabularyAll, n, k, output):
#     f_output = open(output, 'w+')
#     for i in range(len(content)):
#         fVec_token = writeFVHelper(content, i, vocabularyAll, n, k, 0)
#         fVec_stem = writeFVHelper(content, i, vocabularyAll, n, k, 1)
#         fVec_prev = writeFVHelper(content, i, vocabularyAll, n, k, 2)
#         fVec_suff = writeFVHelper(content, i, vocabularyAll, n, k, 3)
#         fVec = fVec_token+fVec_stem+fVec_prev+fVec_suff
#         if len(label) > 0:
#             f_output.write((label[i]) + ',')
#         for i in range(len(fVec) - 1):
#             f_output.write(str(fVec[i]) + ',')
#         f_output.write(str(fVec[len(fVec)-1]) + '\n')
#     f_output.close()

def writeFVHelper(content, i, vocabulary, n, k, switch):
        size = len(content)
        fVec = [0]*(2*n+1)
        # print content[i]
        mid = n
        if switch == 0:
            fVec[mid] = vocabulary[content[i]] if content[i] in vocabulary else 0
        elif switch == 1:
            fVec[mid] = vocabulary[stem(content[i])] if stem(content[i]) in vocabulary else 0
        elif switch == 2:
            s = content[i] if k>len(content[i]) else content[i][:k]
            fVec[mid] = vocabulary[s] if s in vocabulary else 0
        else:
            s = content[i] if k>len(content[i]) else content[i][-k:]
            fVec[mid] = vocabulary[s] if s in vocabulary else 0
        for j in range(1,n+1):
            if i-j >= 0:
                if switch == 0:
                    fVec[mid-j] = vocabulary[content[i-j]] if content[i-j] in vocabulary else 0
                elif switch == 1:
                    fVec[mid-j] = vocabulary[stem(content[i-j])] if stem(content[i-j]) in vocabulary else 0
                elif switch == 2:
                    s = content[i-j] if k>len(content[i-j]) else content[i-j][:k]
                    fVec[mid-j] = vocabulary[s] if s in vocabulary else 0
                else:
                    s = content[i-j] if k>len(content[i-j]) else content[i-j][-k:]
                    fVec[mid-j] = vocabulary[s] if s in vocabulary else 0
            if i+j < size:
                if switch == 0:
                    fVec[mid+j] = vocabulary[content[i+j]] if content[i+j] in vocabulary else 0
                elif switch == 1:
                    fVec[mid+j] = vocabulary[stem(content[i+j])] if stem(content[i+j]) in vocabulary else 0
                elif switch == 2:
                    s = content[i+j] if k>len(content[i+j]) else content[i+j][:k]
                    fVec[mid+j] = vocabulary[s] if s in vocabulary else 0
                else:
                    s = content[i+j] if k>len(content[i+j]) else content[i+j][-k:]
                    fVec[mid+j] = vocabulary[s] if s in vocabulary else 0
        # print fVec
        return fVec

def readTrainFile(input):
    f = open(input, 'r')
    content =[]
    label = []
    f.readline()
    for line in f:
        if len(line.strip())>0 and "-DOCSTART-" not in line:
            words = line.split()
            content.append(words[0])
            label.append(words[-1])
    return content, label

# def readTestFile(input):
#     f = open(input, 'r')
#     content =[]
#     f.readline()
#     for line in f:
#         line = line.split()
#         if len(line) > 0:
#             content.append(line[0])
#     return content

def getData(input, output, tag):
    global vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff
    if tag == 'train':
        content, label = readTrainFile(input)
        vocabulary = getVocabulary(content)
        vocabularyStem = getVocabularyStem(content)
        vocabularyPrev = getVocabularyPrev(content,k)
        vocabularySuff = getVocabularySuff(content,k)
        print((2*n+1)*(len(vocabulary)+len(vocabularyStem)+len(vocabularyPrev)+len(vocabularySuff)))
        writeFeatureVector(content, label, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, k, output)
        # vocabularyAll = getVocabularyAll(content,k)
        # writeFeatureVector(content, label, vocabularyAll, n, k, output)
        # return vocabularyAll
    elif tag == 'test':
        content, label = readTrainFile(input)
        writeFeatureVector(content, label, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, k, output)


def processSentence(content):
    content = removePunctuation(content)
    content = content.split()
    return getFeatureVector(content, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, k)

# f = readfile('input')
# content, label = readfile('eng.train.txt')
# print len(content)
# print len(label)

if __name__ == '__main__':
    getData('eng.train.txt', 'output', 'train')
    getData('eng.test.txt', 'output_test', 'test')
    result = processSentence('This is')
    # result = getTestData('This is', n, k, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff)
    print(result)

# # content_withoutPunc = removePunctuation(fileContent)
# # print content_withoutPunc
# #
# vocabulary = getVocabulary(content)
# # print vocabulary
# #
# vocabularyStem = getVocabularyStem(content)
# # print vocabularyStem
# #
# vocabularyPrev = getVocabularyPrev(content,k)
# # print vocabularyPrev
# #
# vocabularySuff = getVocabularySuff(content,k)
# # print vocabularySuff
# #
# writeFeatureVector(content, label, vocabulary, vocabularyStem, vocabularyPrev, vocabularySuff, n, 'output')