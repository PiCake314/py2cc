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



template <typename T, typename U>
auto add(const T& a, const U& b) {
	return a + b;
}



int main()
{
	std::setprecision(2);
	std::println("{}", add(1, 2));
}


