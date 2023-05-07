#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

pair<int, int> slide(
    const vector<string>& board,
    const pair<int, int>& pos,
    const string& direction,
    const map<string, pair<int, int>>& pieces)
{
    map<string, pair<int, int>> direction_map = { { "Up", { -1, 0 } }, { "Down", { 1, 0 } }, { "Left", { 0, -1 } }, { "Right", { 0, 1 } } };
    auto [dy, dx] = direction_map[direction];
    auto [y, x] = pos;

    while (true) {
        int ny = y + dy;
        int nx = x + dx;
        if (!(0 <= ny && ny < int(board.size()) && 0 <= nx && nx < int(board[0].size()))) {
            break;
        }
        if (board[ny][nx] == '#') {
            break;
        }
        if (find_if(pieces.begin(), pieces.end(), [ny, nx](const auto& kvp) { return kvp.second == make_pair(ny, nx); }) != pieces.end()) {
            break;
        }
        y = ny;
        x = nx;
    }

    return { y, x };
}

string convert_to_state(const map<string, pair<int, int>>& pieces)
{
    string state;
    for (const auto& [piece, pos] : pieces) {
        state += piece + to_string(pos.first) + "," + to_string(pos.second) + ";";
    }
    return state;
}

vector<pair<string, string>> solve(
    const vector<string>& board,
    map<string, pair<int, int>> pieces,
    const map<string, pair<int, int>>& goals)
{
    queue<pair<map<string, pair<int, int>>, vector<pair<string, string>>>> search_queue;
    search_queue.push({ pieces, {} });
    unordered_set<string> visited;
    visited.insert(convert_to_state(pieces));

    while (!search_queue.empty()) {
        auto [cur_pieces, path] = search_queue.front();
        search_queue.pop();

        if (cur_pieces == goals) {
            return path;
        }

        for (const auto& [piece, pos] : cur_pieces) {
            for (const auto& direction : { "Up", "Down", "Left", "Right" }) {
                map<string, pair<int, int>> new_pieces = cur_pieces;
                new_pieces[piece] = slide(board, pos, direction, new_pieces);
                string new_state = convert_to_state(new_pieces);
                if (visited.find(new_state) == visited.end()) {
                    visited.insert(new_state);
                    search_queue.push({ new_pieces, path });
                    search_queue.back().second.push_back({ piece, direction });
                }
            }
        }
    }

    return {};
}

int main()
{
    int rows, cols, num_pieces;
    cin >> rows >> cols >> num_pieces;
    vector<string> board(rows);
    for (int i = 0; i < rows; ++i) {
        cin >> board[i];
    }

    map<string, pair<int, int>> pieces;
    map<string, pair<int, int>> goals;
    for (int i = 0; i < num_pieces; ++i) {
        string piece_name;
        int py, px, gy, gx;
        cin >> piece_name >> py >> px >> gy >> gx;
        pieces[piece_name] = { py, px };
        goals[piece_name] = { gy, gx };
    }

    auto path = solve(board, pieces, goals);
    if (path.empty()) {
        cout << "Done: Unsolvable\n";
    } else {
        for (int i = 0; i < int(path.size()); ++i) {
            auto [piece, direction] = path[i];
            cout << i + 1 << '\t' << piece << '\t' << direction << '\n';
        }
        cout << "Done: " << path.size() << " steps\n";
    }

    return 0;
}
