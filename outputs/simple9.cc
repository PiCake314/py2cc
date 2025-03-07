#include <print>
#include <string>
#include <vector>
#include <ranges>

using namespace std::literals;


int main() {
	auto cond = 1 < 3;
	if (cond) std::println("{}", "YES!"s);
}


