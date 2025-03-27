#include <print>
#include <iomanip>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <tuple>
#include <utility>
#include <ranges>

#include <optional>
#include <variant>
#include <any>


using std::operator""s;






int main()
{
	std::setprecision(2);
	bool cond1 = true and true or false;
	int cond2 = not cond1;
	std::string x = cond1 ? "Hi"s : "Hello"s;
	int y = cond2 ? 1 : 2;
	std::println("{} {}", x, y);
}


