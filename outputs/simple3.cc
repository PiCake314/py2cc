#include <print>
#include <string>
#include <ranges>

using namespace std::literals;


int main() {
	auto a = "Hello"s;
	auto b = "World"s;
	std::println("{}", a + ", "s + b + "!"s);
}


