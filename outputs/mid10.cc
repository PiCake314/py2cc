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
	std::vector x = std::vector{"a"s, "b"s, "c"s, "x"s, "y"s, "z"s};			// ctad takes care of type parameter deduction
	for (const auto& elt : x) {
		if (elt == "x"s or elt == "b"s) continue;
		std::println("{}", elt);
	}
	std::println("{}", "done!"s);
}


