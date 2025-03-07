#include <print>
#include <string>
#include <ranges>

using namespace std::literals;


int main() {
	auto name = "Ali"s;
	auto age = 23;
	std::println("{} {} {}", "Hello, my name is "s + name + " and I am"s, age, "years old"s);
}


