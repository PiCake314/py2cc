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



template <typename T>
auto greet(const T& name) {
	std::println("{} {}", "Hello,"s, name);
}



int main()
{
	std::setprecision(2);
	greet("Ali"s);
}


