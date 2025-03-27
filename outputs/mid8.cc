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
	std::vector v = std::vector{"Hey!"s, "Name is"s, "aliiii"s};			// ctad takes care of type parameter deduction
	for (const auto& e : v) std::println("{}", e);
}


