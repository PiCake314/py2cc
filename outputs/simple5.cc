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
	int x = +10;
	int y = -x;
	int z = +x;
	bool a = true;
	int b = not a;
	int c = -1;
	int d = ~c;
	std::println("{}", x);
	std::println("{}", y);
	std::println("{}", z);
	std::println("{}", a);
	std::println("{}", b);
	std::println("{}", c);
	std::println("{}", d);
}


