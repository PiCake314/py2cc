#include <print>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <tuple>
#include <ranges>

using namespace std::literals;


auto add(const auto& a, const auto& b) {
	return a + b;
}



int main()
{
	std::println("{}", add(1, 2));
}


