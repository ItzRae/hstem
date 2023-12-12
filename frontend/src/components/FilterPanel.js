import React, { useState } from "react";
import {
  Box,
  Checkbox,
  CheckboxGroup,
  Input,
  Button,
  Flex,
  Spacer,
  VStack,
  HStack,
} from "@chakra-ui/react";

const FilterPanel = ({ onFilter, projects }) => {
  const [selectedExtensions, setSelectedExtensions] = useState([]);
  const [selectedMajors, setSelectedMajors] = useState([]);
  const [startYear, setStartYear] = useState("");
  const [endYear, setEndYear] = useState("");

  const extensions = [...new Set(projects.map((project) => project.extension))];
  const majors = [
    ...new Set(
      projects
        .map((project) => project.major)
        .filter((major) => major) // Filter truthy values (non-empty strings)
        .flatMap((major) => major.split(", "))
    ),
  ];

  const handleFilter = () => {
    if (onFilter) {
      onFilter({
        extensions: selectedExtensions,
        majors: selectedMajors,
        startYear,
        endYear,
      });
    }
  };

  return (
    <Box p="4" bg="gray.200" borderRadius="md" boxShadow="md">
      <VStack spacing="4" maxH="200px">
        <CheckboxGroup
          value={selectedExtensions}
          onChange={setSelectedExtensions}
        >
          <VStack overflowY="auto">
            {extensions.map((extension) => (
              <Checkbox key={extension} value={extension}>
                {extension}
              </Checkbox>
            ))}
          </VStack>
        </CheckboxGroup>

        <CheckboxGroup value={selectedMajors} onChange={setSelectedMajors}>
          <VStack align="start" overflowY="auto">
            {majors.map((major) => (
              <Checkbox key={major} value={major}>
                {major}
              </Checkbox>
            ))}
          </VStack>
        </CheckboxGroup>
      </VStack>

      <Flex align="center">
        <Input
          type="number"
          placeholder="Start Year"
          value={startYear}
          onChange={(e) => setStartYear(e.target.value)}
          mr="2"
        />
        <Input
          type="number"
          placeholder="End Year"
          value={endYear}
          onChange={(e) => setEndYear(e.target.value)}
          mr="2"
        />
        <Spacer />
      </Flex>
      <Button colorScheme="purple" onClick={handleFilter}>
        Apply Filters
      </Button>
    </Box>
  );
};

export default FilterPanel;
