#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>
// 三维数组：digits[数字0-9][行5][列3]
// 直接硬编码每个数字的 5x3 点阵
using namespace std;

int digits[10][5][3] = {
    // 数字 0
    {{1,1,1},
     {1,0,1},
     {1,0,1},
     {1,0,1},
     {1,1,1}},

    // 数字 1
    {{0,0,1},
     {0,0,1},
     {0,0,1},
     {0,0,1},
     {0,0,1}},

    // 数字 2
    {{1,1,1},
     {0,0,1},
     {1,1,1},
     {1,0,0},
     {1,1,1}},

    // 数字 3
    {{1,1,1},
     {0,0,1},
     {1,1,1},
     {0,0,1},
     {1,1,1}},

    // 数字 4
    {{1,0,1},
     {1,0,1},
     {1,1,1},
     {0,0,1},
     {0,0,1}},

    // 数字 5
    {{1,1,1},
     {1,0,0},
     {1,1,1},
     {0,0,1},
     {1,1,1}},

    // 数字 6
    {{1,1,1},
     {1,0,0},
     {1,1,1},
     {1,0,1},
     {1,1,1}},

    // 数字 7
    {{1,1,1},
     {0,0,1},
     {0,0,1},
     {0,0,1},
     {0,0,1}},

    // 数字 8
    {{1,1,1},
     {1,0,1},
     {1,1,1},
     {1,0,1},
     {1,1,1}},

    // 数字 9
    {{1,1,1},
     {1,0,1},
     {1,1,1},
     {0,0,1},
     {1,1,1}}
};

void printDigit(int d) {
    for (int r = 0; r < 5; ++r) {
        for (int c = 0; c < 3; ++c) {
            std::cout << digits[d][r][c];
        }
        std::cout << '\n';
    }
}
int map[60][60];

// 在map中显示数字的函数
void displayNumberInMap(int startRow, int startCol, int digit) {
    for(int r = 0; r < 5; r++) {
        for(int c = 0; c < 3; c++) {
            map[startRow + r][startCol + c] = digits[digit][r][c];
        }
    }
}

// 打印map的函数
void printMap() {
    for(int r = 0; r < 60; r++) {
        for(int c = 0; c < 60; c++) {
            cout << map[r][c];
        }
        cout << endl;
    }
}

int main() {
    // 初始化map为0
    for(int r = 0; r < 60; r++) {
        for(int c = 0; c < 60; c++) {
            map[r][c] = 0;
        }
    }
    
    // 每次只显示一个数字，并处理对应的maps.csv
    for(int p = 1; p <= 34; p++) {
        if (p==11||p==9)continue;
        cout << "处理Survival_" << p << "..." << endl;
        
        // 清空map
        for(int r = 0; r < 60; r++) {
            for(int c = 0; c < 60; c++) {
                map[r][c] = 0;
            }
        }
        
        // 提取每一位数字
        int a[4];
        int n = p;
        for(int j = 0; j < 4; j++) {
            a[j] = n / (int)pow(10, 3-j);
            n = n % (int)pow(10, 3-j);
        }
        
        // 在map中央显示这个4位数字
        int startRow = 1;
        int startCol = 1;
        
        for(int j = 0; j < 4; j++) {
            int digit = a[j];
            displayNumberInMap(startRow, startCol + j * 4, digit);
        }
        
        // 打印当前数字
        cout << "当前显示数字: " << p << endl;
        
        // 打印整个map
        /*
        for(int r = 0; r <=59; r++) {
            for(int c = 0; c <=59; c++) {
                cout << map[r][c];
            }
            cout << endl;
        }
        cout << endl;
        */
        // 处理maps.csv文件 - 找到Survival_p所在的行并替换
        ifstream file("maps.csv");
        if (!file.is_open()) {
            cout << "无法打开maps.csv文件" << endl;
            continue;
        }
        
        vector<string> lines;
        string line;
        
        // 读取所有行
        while (getline(file, line)) {
            lines.push_back(line);
        }
        file.close();
        
        // 查找Survival_p所在的行
        bool found = false;
        for (size_t i = 0; i < lines.size(); i++) {
            ostringstream oss;
            oss << "Survival_" << p << ",";
            string searchStr = oss.str();
            
            if (lines[i].find(searchStr) == 0) {
                // 找到行，删除后面的内容，只保留Survival_1
                lines[i] = searchStr;
                
                // 删除下面的59行（如果存在的话）
                int linesToDelete = min(59, (int)(lines.size() - i - 1));
                if (linesToDelete > 0) {
                    lines.erase(lines.begin() + i + 1, lines.begin() + i + 1 + linesToDelete);
                }
                
                // 在Survival_1行后面添加第一个60个字符
                string firstRow = "\"";
                for(int c = 0; c < 60; c++) {
                    firstRow += (map[0][c] == 1) ? "1" : "0";
                }
                firstRow += "\",";
                lines[i] += firstRow;
                
                // 插入剩余的59行新内容（总共60行）
                for(int r = 1; r < 60; r++) {
                    string newRow = ",\"";
                    for(int c = 0; c < 60; c++) {
                        newRow += (map[r][c] == 1) ? "1" : "0";
                    }
                    newRow += "\",";
                    
                    // 在Survival_1行后面插入新行
                    lines.insert(lines.begin() + i + 1 + (r-1), newRow);
                }
                
                cout << "已替换Survival_" << p << "，删除了" << linesToDelete << "行，插入了59行新内容，总共60行" << endl;
                found = true;
                break;
            }
        }
        
        if (!found) {
            cout << "未找到Survival_" << p << "行" << endl;
        }
        
        // 写回文件
        ofstream outFile("maps.csv");
        if (outFile.is_open()) {
            for (size_t i = 0; i < lines.size(); i++) {
                outFile << lines[i] << endl;
            }
            outFile.close();
            cout << "已更新maps.csv文件" << endl;
        } else {
            cout << "无法写入maps.csv文件" << endl;
        }
        
        cout << "完成Survival_" << p << "的处理" << endl;
        cout << "----------------------------------------" << endl;
    }
    
    return 0;
}