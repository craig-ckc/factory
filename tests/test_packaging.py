import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('factory_check', ROOT / 'scripts/check.py')
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackagingTests(unittest.TestCase):
    def copy(self):
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        shutil.copytree(ROOT / 'plugins', root / 'plugins')
        for name in ('.agents', '.claude-plugin', '.cursor-plugin'):
            shutil.copytree(ROOT / name, root / name)
        shutil.copy(ROOT / 'README.md', root)
        # Preserve README links to repository-level documentation and evaluations.
        for name in ('docs', 'evaluations', 'scripts'):
            if (ROOT / name).exists():
                shutil.copytree(ROOT / name, root / name)
        return root

    def test_repository_contracts(self):
        self.assertEqual(checker.check(ROOT), [])

    def test_version_drift_is_rejected(self):
        root = self.copy()
        path = root / 'plugins/factory/.cursor-plugin/plugin.json'
        value = json.loads(path.read_text())
        value['version'] = '0.0.1'
        path.write_text(json.dumps(value))
        self.assertTrue(checker.check(root))

    def test_wrong_marketplace_source_is_rejected(self):
        root = self.copy()
        path = root / '.agents/plugins/marketplace.json'
        value = json.loads(path.read_text())
        value['plugins'][0]['source']['path'] = './missing'
        path.write_text(json.dumps(value))
        self.assertTrue(checker.check(root))

    def test_broken_skill_reference_is_rejected(self):
        root = self.copy()
        (root / 'plugins/factory/skills/testing/SKILL.md').write_text(
            (root / 'plugins/factory/skills/testing/SKILL.md').read_text() + '\n[missing](../../absent.md)\n')
        self.assertTrue(checker.check(root))
