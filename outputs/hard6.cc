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
auto greetSpecial(const T& name) {
	if (name == "Ali"s) return "I love youuuu <3"s;
	else if (name == "Nawar"s) return "Nawarii my beloved!"s;
	else return "ew, stranger..go away"s;
}



int main()
{
	std::setprecision(2);
	std::println("{}", greetSpecial("Ali"s));
	std::println("{}", greetSpecial("Nawar"s));
	std::println("{}", greetSpecial("someone"s));
}


