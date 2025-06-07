# Amazon KDP Advertising Tool

A comprehensive tool for KDP self-publishers to analyze advertising reports, optimize campaigns, and discover targeted products with AI-powered insights.

## Features

- **Report Analysis**: Upload and analyze Amazon KDP advertising reports
- **Campaign Optimization**: Get AI-powered recommendations to improve campaign performance
- **Targeted Product Discovery**: Find new product opportunities based on market data
- **Performance Tracking**: Monitor advertising metrics and track improvements over time
- **LLM Integration**: Leverage advanced AI for deep insights and recommendations

## Tech Stack

- **Backend**: Flask API with Python
- **Frontend**: React with a visually stunning UI (to be implemented)
- **Database**: MySQL for data storage
- **AI**: OpenAI GPT integration for intelligent analysis
- **Data Processing**: Pandas and NumPy for report processing

## Getting Started

### Prerequisites

- Python 3.11+
- Node.js 20+ (for frontend)
- MySQL database
- OpenAI API key

### Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/kdp-advertising-tool.git
cd kdp-advertising-tool
```

2. Set up the Python virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

3. Configure environment variables
```bash
cp .env.example .env
# Edit .env with your configuration
```

4. Initialize the database
```bash
# Make sure MySQL is running
# The application will create tables on first run
```

5. Run the backend server
```bash
python src/main.py
```

6. Access the API at http://localhost:5000

## API Endpoints

### Reports

- `POST /api/reports/upload` - Upload a new report
- `GET /api/reports/list` - List all uploaded reports
- `GET /api/reports/<report_id>` - Get report details
- `GET /api/reports/<report_id>/summary` - Get AI-generated report summary
- `DELETE /api/reports/<report_id>/delete` - Delete a report

### Analysis

- `GET /api/analysis/performance/<report_id>` - Analyze campaign performance
- `GET /api/analysis/competitive/<report_id>` - Perform competitive analysis
- `GET /api/analysis/trends/<report_id>` - Analyze performance trends
- `GET /api/analysis/sessions/<user_id>` - Get analysis sessions for a user

### Optimization

- `GET /api/optimization/recommendations/<report_id>` - Get optimization recommendations
- `GET /api/optimization/budget-optimization/<report_id>` - Get budget optimization suggestions
- `GET /api/optimization/keyword-optimization/<report_id>` - Get keyword optimization suggestions
- `GET /api/optimization/bid-suggestions/<report_id>` - Get bid adjustment suggestions
- `GET /api/optimization/negative-keywords/<report_id>` - Get negative keyword suggestions
- `POST /api/optimization/recommendations/<recommendation_id>/implement` - Mark recommendation as implemented
- `POST /api/optimization/recommendations/<recommendation_id>/dismiss` - Dismiss recommendation
- `GET /api/optimization/user/<user_id>/recommendations` - Get all recommendations for a user

## Report Format Support

The tool supports the following Amazon advertising report formats:

- Sponsored Products Campaign Reports
- Sponsored Products Keyword Reports
- Sponsored Brands Campaign Reports
- Search Term Reports

## Development

### Backend Development

The backend is built with Flask and follows a modular structure:

- `src/main.py` - Main application entry point
- `src/models/` - Database models
- `src/routes/` - API routes
- `src/services/` - Business logic services

### Frontend Development

The frontend will be implemented in Phase 5 using React.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

