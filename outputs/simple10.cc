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
	std::println("{}", 1 < 2 and 2 < 3);
	std::println("{}", 1 < 2 < 3);
	std::println("{}", 1 < (2 < 3));
	std::println("{}", 1 < 5 and 5 > 2 and 2 < 1);
	std::println("{}", 1 < 5 and 5 > 2 and 2 > 1);
}


