#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main() {
	auto x = true;
	auto y = false;
	std::println("{}", x or y);
	std::println("{}", x and y);
}


