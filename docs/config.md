
# Configuration Guide

## Environment Variables

- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `SECRET_KEY`: Flask application secret key
- `DEBUG`: Enable/disable debug mode

## Theme Customization

The application theme can be customized through `theme.json`:

```json
{
  "variant": "professional",
  "primary": "hsl(222.2 47.4% 11.2%)",
  "appearance": "light",
  "radius": 0.5
}
```

## CSS Variables

Content customization is available through CSS variables in `client/public/styles.css`:

- `--left-panel-title`: Left panel heading
- `--right-panel-title`: Right panel heading
- Additional text variables for panel content

## Development Workflows

The project includes multiple workflows for development:
- `Dev Server`: Main development server
- `Start application`: Production server with Gunicorn
