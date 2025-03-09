#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;

auto greetSpecial(const auto& name) {
	if (name == "Ali"s) return "I love youuuu <3"s;
	else if (name == "Nawar"s) return "Nawarii my beloved!"s;
	else return "ew, stranger..go away"s;
}

int main()
{
	std::println("{}", greetSpecial("Ali"s));
	std::println("{}", greetSpecial("Nawar"s));
	std::println("{}", greetSpecial("Bitch"s));
}


