#include <print>
#include <string>
#include <ranges>

using namespace std::literals;


int main() {
	auto x = 2;
	auto y = 5;
	std::println("{}", x | y);
}


