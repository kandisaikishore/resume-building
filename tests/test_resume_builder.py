import unittest

from src.resume_builder import build_resume, validate_input


class ResumeBuilderTests(unittest.TestCase):
    def setUp(self):
        self.valid_data = {
            "name": "Alex Morgan",
            "title": "Software Engineer",
            "email": "alex@example.com",
            "location": "Austin, TX",
            "summary": "Builds reliable services.",
            "skills": ["Python", "SQL"],
            "experience": [
                {
                    "role": "Engineer",
                    "company": "Acme",
                    "start": "2022",
                    "end": "Present",
                    "highlights": ["Improved CI speed."],
                }
            ],
            "education": [
                {"degree": "B.S. CS", "school": "UT Austin", "year": "2019"}
            ],
        }

    def test_build_resume_contains_sections(self):
        result = build_resume(self.valid_data)
        self.assertIn("# Alex Morgan", result)
        self.assertIn("## Skills", result)
        self.assertIn("## Experience", result)

    def test_validate_input_missing_required_field_raises(self):
        invalid = dict(self.valid_data)
        invalid.pop("email")
        with self.assertRaises(ValueError):
            validate_input(invalid)


if __name__ == "__main__":
    unittest.main()
